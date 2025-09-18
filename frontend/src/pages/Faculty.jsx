// frontend/src/pages/Faculty.jsx
import React, {useState, useEffect, useRef} from 'react'
import QRCode from 'qrcode.react'
import { createSession } from '../api'

function Faculty(){
  const [qr, setQr] = useState('')
  const [course, setCourse] = useState('Demo Course')
  const [sessionId, setSessionId] = useState(null)
  const [attendees, setAttendees] = useState([]) // array of {student_id, timestamp ...}
  const wsRef = useRef(null)

  const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'
  const WS_BASE = API_BASE.replace(/^http/, 'ws')

  const handleCreate = async () => {
    const res = await createSession({teacher_id: 1, course})
    const t = res.data.qr_token || 'demo-qrcode-token'
    const session_id = res.data.session_id || 1
    setQr(t)
    setSessionId(session_id)
  }

  // When sessionId is set, open websocket
  useEffect(()=> {
    if(!sessionId) return
    const wsUrl = `${WS_BASE}/ws/session/${sessionId}`
    const ws = new WebSocket(wsUrl)
    wsRef.current = ws

    ws.onopen = () => {
      console.log('WS connected to session', sessionId)
      // Optionally send a hello or an auth token
      // ws.send(JSON.stringify({type: 'hello', role: 'faculty'}))
    }

    ws.onmessage = (evt) => {
      try {
        const msg = JSON.parse(evt.data)
        if(msg.type === 'attendance_marked') {
          const d = msg.data
          // append to attendee list
          setAttendees(prev => {
            const exists = prev.find(x => x.student_id === d.student_id)
            if(exists) return prev.map(x => x.student_id === d.student_id ? {...x, ...d} : x)
            return [...prev, d]
          })
        }
      } catch (err) {
        console.error('WS message parse error', err)
      }
    }

    ws.onclose = () => { console.log('WS closed') }
    ws.onerror = (e) => { console.error('WS error', e) }

    return () => {
      ws.close()
      wsRef.current = null
    }
  }, [sessionId])

  return (
    <div>
      <h2>Faculty Panel</h2>
      <div>
        <input value={course} onChange={e=>setCourse(e.target.value)} />
        <button onClick={handleCreate}>Create Session</button>
      </div>
      {qr && (
        <div style={{marginTop:20}}>
          <p>Session ID: {sessionId}</p>
          <p>QR Token: {qr}</p>
          <QRCode value={qr} />
        </div>
      )}

      <div style={{marginTop:20}}>
        <h3>Live Attendance</h3>
        <p>Connected attendees: {attendees.length}</p>
        <ul>
          {attendees.map(a => (
            <li key={a.student_id}>
              Student: {a.student_id} — {a.detail || 'present'}
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export default Faculty
