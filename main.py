import random
import typing
import uuid

import locust
import gevent
import grpc
import rpc
import interceptor

import grpc.experimental.gevent as grpc_gevent

grpc_gevent.init_gevent()

FLOW_VACANCIES_PERIOD = 30
LIST_VACANCIES_PERIOD = 40
REQUEST_TIMEOUT = 5  # in seconds


class VacancyUser(locust.User):
    wait_time = locust.constant(FLOW_VACANCIES_PERIOD)

    def __init__(self, environment):
        super().__init__(environment)

        grpc_channel = grpc.insecure_channel(self.host)
        self._channel = grpc.intercept_channel(
            grpc_channel,
            interceptor.LocustGRPCInterceptor(environment=environment),
        )

        self._auth_stub = rpc.AuthServiceStub(self._channel)
        self._vacancy_stub = rpc.VacancyServiceStub(self._channel)

        self._fetch_vacancies_task = None

    def _vacancy(self) -> dict[str, typing.Any]:
        """Generate vacancy with random data."""

        return {
            'Title': f'Title {uuid.uuid4()}',
            'Description': f'Description {uuid.uuid4()}',
            'Division': random.randint(0, 3),
            'Country': random.choice(['Canada', 'USA', 'Mexico']),
        }

    def _create_vacancy(self) -> rpc.Vacancy:
        """Create a vacancy with the given id."""

        create_vacancy_request = rpc.CreateVacancyRequest(**self._vacancy())
        response = self._vacancy_stub.CreateVacancy(
            create_vacancy_request,
            timeout=REQUEST_TIMEOUT,
        )
        return response.vacancy

    def _update_vacancy(self, vacancy: rpc.Vacancy) -> rpc.Vacancy:
        """Update a vacancy with the given id."""

        update_vacancy_request = rpc.UpdateVacancyRequest(
            Id=vacancy.Id,
            Views=vacancy.Views + 1,
            **self._vacancy(),
        )
        response = self._vacancy_stub.UpdateVacancy(
            update_vacancy_request,
            timeout=REQUEST_TIMEOUT,
        )
        return response.vacancy

    def _get_vacancy(self, vacancy_id: str) -> rpc.Vacancy:
        """Get a vacancy with the given id."""

        get_vacancy_request = rpc.VacancyRequest(Id=vacancy_id)
        response = self._vacancy_stub.GetVacancy(
            get_vacancy_request,
            timeout=REQUEST_TIMEOUT,
        )
        return response.vacancy

    def _delete_vacancy(self, vacancy_id: str) -> bool:
        """Delete a vacancy with the given id."""

        delete_vacancy_request = rpc.VacancyRequest(Id=vacancy_id)
        response = self._vacancy_stub.DeleteVacancy(
            delete_vacancy_request,
            timeout=REQUEST_TIMEOUT,
        )
        return response.success

    def _fetch_vacancies(self):
        """Fetch all vacancies, page by page."""

        while True:
            vacancies = []
            page = 1
            limit = 1000

            while True:
                list_vacancies_request = rpc.GetVacanciesRequest(page=page, limit=limit)
                page_vacancies = [
                    vacancy
                    for vacancy in self._vacancy_stub.GetVacancies(
                        list_vacancies_request,
                    )
                ]

                # Break if the current page is empty
                if not page_vacancies:
                    break

                page += 1
                vacancies.extend(page_vacancies)

            gevent.sleep(LIST_VACANCIES_PERIOD)

    @locust.task
    def vacancy_flow(self):
        new_vacancy = self._create_vacancy()
        updated_vacancy = self._update_vacancy(new_vacancy)
        vacancy = self._get_vacancy(updated_vacancy.Id)
        self._delete_vacancy(vacancy.Id)

    def on_start(self):
        self._fetch_vacancies_task = gevent.spawn(self._fetch_vacancies)

    def on_stop(self):
        if self._fetch_vacancies_task is not None:
            self._fetch_vacancies_task.kill()

        self._channel.close()


if __name__ == '__main__':
    locust.run_single_user(VacancyUser)
