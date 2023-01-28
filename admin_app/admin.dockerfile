FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/workdir
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./admin_panel admin_panel
COPY --chown=${USER} --chmod=755 ./start.sh /start.sh

USER ${USER}

ENTRYPOINT ["/start.sh"]

CMD ["python", "admin_panel/manage.py", "runserver"]
