FROM python
WORKDIR /app
COPY . /app/
EXPOSE 8000
CMD ["bash"]
