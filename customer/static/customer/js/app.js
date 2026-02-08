const form = document.getElementById("studentForm");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        educations: [
            {
                degree: document.getElementById("degree").value,
                institution_name: document.getElementById("institution").value,
                passing_year: document.getElementById("passing_year").value,
                result: document.getElementById("result").value
            }
        ]
    };

    fetch("/api/students/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        alert("Student Created Successfully!");
        console.log(result);
        form.reset();
    })
    .catch(error => {
        console.error(error);
    });
});
