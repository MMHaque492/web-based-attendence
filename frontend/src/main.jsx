import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Student from './pages/Student'
import Faculty from './pages/Faculty'
import Admin from './pages/Admin'
import './styles.css'


function App(){
return (
<BrowserRouter>
<div style={{padding:20}}>
<nav style={{marginBottom:20}}>
<Link to="/student">Student</Link> | <Link to="/faculty">Faculty</Link> | <Link to="/admin">Admin</Link>
</nav>
<Routes>
<Route path="/" element={<Student/>} />
<Route path="/student" element={<Student/>} />
<Route path="/faculty" element={<Faculty/>} />
<Route path="/admin" element={<Admin/>} />
</Routes>
</div>
</BrowserRouter>
)
}


createRoot(document.getElementById('root')).render(<App />)
