import { useState } from 'react'
import './App.css'
import Sandbox from './Components/sandbox'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className='w-100 h-100'>
        <Sandbox/>
      </div>
    </>
  )
}

export default App
