FROM python
WORKDIR /my-shopping-proj

RUN pip install -U virtualenv 
RUN pip install flask


RUN virtualenv venv
ENV VIRTUAL_ENV /venv
ENV PATH /venv/bin:$PATH
RUN /bin/bash -c "source venv/bin/activate"

EXPOSE 5000
#RUN virtualenv venv

#WORKDIR /venv && source venv/bin/activate 
#RUN source venv/bin/activate 
#WORKDIR /my-shopping-proj

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

RUN pip install -r requirements.txt

# Run the application:
COPY app.py .
CMD ["python3.6", "app.py"]
