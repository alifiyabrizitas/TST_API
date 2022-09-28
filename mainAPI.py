#NAMA : Alifiya Brizita Shary
#NIM : 18220069


from http.client import HTTPException
from fastapi import FastAPI
import json


with open("mahasiswa.json", "r") as read_file:
    data = json.load(read_file)

app = FastAPI()

#Menampilkan dan mencari nama mahasiswa dengan NIM
#NIM Sudah terdaftar pada data json yang telah dibuat


@app.get("/get-by-NIM/{nim}")
def read_mahasiswa(nim: int):
    for data_mahasiswa in data['mahasiswa']:
        if data_mahasiswa['NIM'] == nim:
            return data_mahasiswa
    return { "Data" : "NOT FOUND"}

#Menampilkan data json yang telah dibuat pada root

@app.get("/")
def root():
    return data
