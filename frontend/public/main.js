const API_URL = "http://127.0.0.1:8000/students/";

document.addEventListener("DOMContentLoaded", () => {
    loadStudents();
    document.getElementById("studentForm").addEventListener("submit", addStudent);
});

// ฟังก์ชันโหลดรายชื่อนักเรียน
async function loadStudents() {
    const res = await fetch(API_URL);
    const students = await res.json();
    const tbody = document.querySelector("#studentsTable tbody");
    tbody.innerHTML = "";

    students.forEach(student => {
        const row = `
            <tr>
                <td>${student.id}</td>
                <td>${student.first_name}</td>
                <td>${student.last_name}</td>
                <td>${student.email}</td>
                <td>${student.phone}</td>
            </tr>`;
        tbody.innerHTML += row;
    });
}

// ฟังก์ชันเพิ่มนักเรียนใหม่
async function addStudent(event) {
    event.preventDefault();

    const data = {
        first_name: document.getElementById("first_name").value,
        last_name: document.getElementById("last_name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value
    };

    const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    if (res.ok) {
        alert("✅ Student added successfully!");
        loadStudents();
        event.target.reset();
    } else {
        alert("❌ Failed to add student");
    }
}
