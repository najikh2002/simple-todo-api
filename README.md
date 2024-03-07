  Dokumentasi API Todo

  __Base URL:__ [https://simple-todo-api-vde6.onrender.com](https://simple-todo-api-vde6.onrender.com)

1\. Mendapatkan Semua Tugas
===========================

### Request

*   **URL:** /todos
*   **Method:** GET

### Response

*   **Status Code:** 200 OK
*   **Body:**

{
  "todos": \[
    {"id": 1, "task": "Belajar Python", "done": false},
    {"id": 2, "task": "Membuat API", "done": false},
    {"id": 3, "task": "Deploy ke Render", "done": false}
  \]
}

2\. Mendapatkan Tugas Berdasarkan ID
====================================

### Request

*   **URL:** /todos/{todo\_id}  
    (Gantilah {todo\_id} dengan ID tugas yang diinginkan.)
*   **Method:** GET

### Response

*   **Status Code:**

*   200 OK jika tugas ditemukan.
*   404 Not Found jika tugas tidak ditemukan.

*   **Body (jika ditemukan):**

{
  "todo": {"id": 1, "task": "Belajar Python", "done": false}
}

*   **Body (jika tidak ditemukan):**

{"message": "Tugas tidak ditemukan"}

3\. Menambahkan Tugas Baru
==========================

### Request

*   **URL:** /todos
*   **Method:** POST
*   **Body:**

{"task": "Nama Tugas Baru"}

### Response

*   **Status Code:** 200 OK
*   **Body:**

{
  "message": "Tugas berhasil ditambahkan",
  "todo": {"id": 4, "task": "Nama Tugas Baru", "done": false}
}

4\. Mengubah Status Tugas Menjadi Selesai
=========================================

### Request

*   **URL:** /todos/{todo\_id}  
    (Gantilah {todo\_id} dengan ID tugas yang diinginkan.)
*   **Method:** PUT

### Response

*   **Status Code:**

*   200 OK jika tugas ditemukan dan status diubah.
*   404 Not Found jika tugas tidak ditemukan.

*   **Body (jika ditemukan dan diubah):**

{
  "message": "Status tugas berhasil diubah",
  "todo": {"id": 1, "task": "Belajar Python", "done": true}
}

*   **Body (jika tidak ditemukan):**

{"message": "Tugas tidak ditemukan"}

5\. Menghapus Tugas
===================

### Request

*   **URL:** /todos/{todo\_id}  
    (Gantilah {todo\_id} dengan ID tugas yang diinginkan.)
*   **Method:** DELETE

### Response

*   **Status Code:**

*   200 OK jika tugas ditemukan dan dihapus.
*   404 Not Found jika tugas tidak ditemukan.

*   **Body (jika ditemukan dan dihapus):**

{"message": "Tugas berhasil dihapus"}

*   **Body (jika tidak ditemukan):**

{"message": "Tugas tidak ditemukan"}

Catatan:
--------

*   Semua data dikembalikan dalam format JSON.
*   Jika terjadi kesalahan, pesan kesalahan akan dikembalikan bersama dengan status code yang sesuai.
*   Gunakan metode HTTP yang benar (GET, POST, PUT, DELETE) sesuai dengan tindakan yang diinginkan.
