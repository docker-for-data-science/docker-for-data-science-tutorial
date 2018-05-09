FROM python:3.6
ENV PATH="/app/.local/bin/:${PATH}"
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


EXPOSE 8888
EXPOSE 9000

CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
