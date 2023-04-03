FROM python:3-alpine

#COPY ./requirements.txt /app/requirements.txt

#WORKDIR /Mortgage

RUN apk --update add python3 py3-pip openssl ca-certificates py-openssl wget git linux-headers
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python3-dev py3-pip build-base \
  && pip install --upgrade pip \
  && pip install --upgrade pipenv\
  && pip install --upgrade tornado\
  && pip install --upgrade requests\
  && apk del build-dependencies

#COPY . /Mortgage

RUN git clone https://github.com/JeevanNaikOP/CreditWorthinessEvaluation.git

WORKDIR CreditWorthinessEvaluation

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]