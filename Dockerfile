FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python", "app.py"]
FROM nginx:latest
COPY website.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html