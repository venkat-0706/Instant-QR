const qrText = document.getElementById('qrText');
const qrImage = document.getElementById('qrImage');
const generateBtn = document.getElementById('generateBtn');
const downloadBtn = document.getElementById('downloadBtn');

generateBtn.addEventListener('click', () => {
    const text = qrText.value.trim();
    if (!text) {
        alert('Please enter some text.');
        return;
    }
    // Generate QR code image using api.qrserver.com
    qrImage.style.display = 'block';
    qrImage.src = `https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=${encodeURIComponent(text)}&bgcolor=fff&color=003366`;

    qrImage.onload = () => {
        downloadBtn.style.display = 'inline-block';
        downloadBtn.href = qrImage.src;
    };
});
