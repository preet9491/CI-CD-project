
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Temporary storage for this beginner project
students = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Registration</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            margin: 0;
            padding: 30px 15px;
        }
        .container {
            max-width: 500px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 15px #0001;
        }
        h1 { color: #2457a7; text-align: center; }
        input, select, button {
            box-sizing: border-box;
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border-radius: 6px;
            border: 1px solid #ccc;
        }
        button {
            background: #2457a7;
            color: white;
            cursor: pointer;
            border: none;
        }
        .student {
            background: #edf7ed;
            padding: 10px;
            margin-top: 10px;
            border-radius: 6px;
            overflow-wrap: anywhere;
        }
        .error { color: #b00020; }
    </style>
</head>
<body>
<div class="container">
    <h1>Student Registration</h1>
    <p>Fill in your details below.</p>

    <form method="POST">
        <input name="name" placeholder="Student Name" required>
        <input name="email" type="email" placeholder="Email Address" required>

        <select name="course" required>
            <option value="">Select Course</option>
            <option value="BCA">BCA</option>
            <option value="BBA">BBA</option>
            <option value="BCom">BCom</option>
            <option value="MCA">MCA</option>
        </select>

        <button type="submit">Register Student</button>
    </form>

    {% if message %}
        <p class="error">{{ message }}</p>
    {% endif %}

    <h2>Registered Students</h2>
    {% for student in students %}
        <div class="student">
            <strong>{{ student.name }}</strong><br>
            {{ student.email }}<br>
            Course: {{ student.course }}
        </div>
    {% else %}
        <p>No students registered yet.</p>
    {% endfor %}
</div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        course = request.form.get("course", "").strip()

        if not name or not email or course not in {
            "BCA", "BBA", "BCom", "MCA"
        }:
            message = "Please enter valid registration details."
        else:
            students.append({
                "name": name,
                "email": email,
                "course": course
            })

    return render_template_string(
        HTML, students=students, message=message
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
