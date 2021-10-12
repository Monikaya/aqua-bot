FROM gorialis/discord.py

WORKDIR /container

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
