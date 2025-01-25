document.getElementById('uploadButton').addEventListener('click', function() {
    var fileInput = document.getElementById('fileInput').files[0];
    if(!fileInput) {
        alert('Please select a file!');
        return;
    }

    var formData = new FormData();
    formData.append('file', fileInput);

    // 업로드한 이미지 미리보기
    var reader = new FileReader();
    reader.onload = function(e) {
        var uploadedImage = document.getElementById('uploadedImage');
        uploadedImage.src = e.target.result;
        uploadedImage.style.display = 'block'; // 이미지 표시
        uploadedImage.style.width = '400px'; // 너비를 400px로 설정
        uploadedImage.style.height = '400px'; // 높이를 400px로 설정정
    };
    reader.readAsDataURL(fileInput) // 파일 읽기

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if(data.prediction !== undefined) {
            document.getElementById('result').innerText = 'Prediction: ' + data.prediction;
        } else {
            document.getElementById('result').innerText = 'Error: ' + (data.error || 'Unknown error');
        }
    })
    .catch(error => {
        console.error('Error: ', error);
        document.getElementById('result').innerText = 'Error occurred during prediction';
    })
})