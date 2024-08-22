#!q node

// Required parameters:
// @raycast.schemaVersion 1
// @raycast.title Add article to Yggdrasil
// @raycast.mode compact

// Optional parameters:
// @raycast.icon 🤖

console.log('aaa');

/*
const https = require('https');
const { execSync } = require('child_process');

// Function to read the clipboard content
function getClipboard() {
  return execSync('pbpaste').toString().trim();
}

// Function to send the HTTP request
function sendUrl(url) {
  const options = {
    hostname: 'https://hook.eu1.make.com', // Replace with your server
    port: 443, // Use 80 for HTTP
    path: `/q9vonnupnacoaticiaeokwbgk78tyaoz?url=${encodeURIComponent(url)}`,
    method: 'GET'
  };

  const req = https.request(options, res => {
    let data = '';

    res.on('data', chunk => {
      data += chunk;
    });

    res.on('end', () => {
      console.log(`Response: ${data}`);
    });
  });

  req.on('error', error => {
    console.error(`Error: ${error.message}`);
  });

  req.end();
}

const clipboardUrl = getClipboard();
if (clipboardUrl) {
  sendUrl(clipboardUrl);
} else {
  console.error('Clipboard does not contain a valid URL.');
}

 */
