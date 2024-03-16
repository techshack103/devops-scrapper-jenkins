FROM python
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN playwright install
RUN playwright install-deps
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]