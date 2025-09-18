import React, {useState, useRef} from 'react'
import { login, markAttendance, verifyFace } from '../api'
import WebcamCapture from '../components/WebcamCapture'
import Html5QrcodeScanner from 'html5-qrcode'


function Student(){
const [email, setEmail] = useState('student@example.com');
const [token, setToken] = useState('');
const [message, setMessage] = useState('');
const webcamRef = useRef();


const handleLogin = async () => {
try{
const res = await login(email, 'device-demo');
setToken(res.data.access_token || 'fake-token')
setMessage('Logged in (stub)')
}catch(err){ setMessage('login error') }
}


const startQrScanner = () => {
const html5QrCode = new Html5QrcodeScanner("qr-reader", { fps: 10, qrbox: 250 });
html5QrCode.render(async (decodedText, decodedResult) => {
// called when a QR code is read
setMe