FROM python:3.10.7

RUN mkdir /code
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install "setuptools==57.5.0"
RUN pip install -r requirements.txt

COPY ./ /code

EXPOSE 8001

ENTRYPOINT [ "/code/entrypoint_dev.sh" ]