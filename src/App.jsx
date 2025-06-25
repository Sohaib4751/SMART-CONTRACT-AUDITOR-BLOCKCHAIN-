import UploadForm from "./components/uploadform";
import Dashboard from "./components/dashboard";
import { useEffect, useRef } from 'react';


function App() {
  const leftChainRef = useRef(null);
  const rightChainRef = useRef(null);


  useEffect(() => {
    const animateChains = () => {
      if (leftChainRef.current && rightChainRef.current) {
        const speed = 0.5;
        let position = 0;
       
        const animate = () => {
          position += speed;
          leftChainRef.current.style.transform = `translateY(${position}px)`;
          rightChainRef.current.style.transform = `translateY(${position}px)`;
         
          if (position >= 100) {
            position = -100;
          }
          requestAnimationFrame(animate);
        };
        animate();
      }
    };


    animateChains();
  }, []);


  return (
    <div className="min-h-screen bg-black text-cyan-400 font-mono flex flex-col items-center px-4 py-10 relative overflow-hidden">
      {/* Animated Left Chain */}
      <div
        ref={leftChainRef}
        className="absolute left-4 top-0 h-full w-8 opacity-30 pointer-events-none"
        style={{ backgroundImage: 'url("data:image/svg+xml,%3Csvg width=\'32\' height=\'100\' viewBox=\'0 0 32 100\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M16 0L32 15V30L16 45L0 30V15L16 0Z\' fill=\'%2300ffff\'/%3E%3Cpath d=\'M16 50L32 65V80L16 95L0 80V65L16 50Z\' fill=\'%2300ffff\'/%3E%3C/svg%3E")' }}
      ></div>


      {/* Animated Right Chain */}
      <div
        ref={rightChainRef}
        className="absolute right-4 top-0 h-full w-8 opacity-30 pointer-events-none"
        style={{ backgroundImage: 'url("data:image/svg+xml,%3Csvg width=\'32\' height=\'100\' viewBox=\'0 0 32 100\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M16 0L32 15V30L16 45L0 30V15L16 0Z\' fill=\'%2300ffff\'/%3E%3Cpath d=\'M16 50L32 65V80L16 95L0 80V65L16 50Z\' fill=\'%2300ffff\'/%3E%3C/svg%3E")' }}
      ></div>


      {/* Hexagonal Background (Smaller) */}
      <div className="absolute inset-0 opacity-[10%] pointer-events-none">
        <svg width="100%" height="100%">
          <defs>
            <pattern id="hex-pattern" width="24" height="20.8" patternUnits="userSpaceOnUse">
              <path
                d="M6 0L18 0L24 10.4L18 20.8L6 20.8L0 10.4Z"
                fill="none"
                stroke="currentColor"
                strokeWidth="0.6"
              />
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#hex-pattern)" />
        </svg>
      </div>


      {/* Main Content (Unchanged) */}
      <div className="relative z-10 w-full max-w-md mx-auto flex flex-col items-center">
        {/* Lock Icon Section */}
        <div className="mb-10 text-center relative">
          <div className="absolute inset-0 rounded-full bg-cyan-400/20 blur-xl animate-pulse w-[140px] h-[140px] mx-auto top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2"></div>
          <div className="relative">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              className="w-24 h-24 text-cyan-400 mx-auto drop-shadow-[0_0_10px_rgba(34,211,238,0.8)]"
            >
              <path
                fillRule="evenodd"
                d="M12 1.5a5.25 5.25 0 0 0-5.25 5.25v3a3 3 0 0 0-3 3v6.75a3 3 0 0 0 3 3h10.5a3 3 0 0 0 3-3v-6.75a3 3 0 0 0-3-3v-3c0-2.9-2.35-5.25-5.25-5.25zm3.75 8.25v-3a3.75 3.75 0 1 0-7.5 0v3h7.5z"
                clipRule="evenodd"
              />
            </svg>
          </div>
          <h1 className="text-3xl md:text-4xl font-bold mt-4 tracking-tight text-cyan-400 relative z-10">
            SMART CONTRACT AUDITOR
          </h1>
        </div>


        <UploadForm />
        <Dashboard />


        {/* Bottom Hexagons */}
        <div className="mt-12 flex justify-center space-x-3">
          {[...Array(5)].map((_, i) => (
            <svg
              key={i}
              viewBox="0 0 120 104"
              width="30"
              height="26"
              className="text-cyan-400 opacity-70"
            >
              <path
                d="M30 0L90 0L120 52L90 104L30 104L0 52Z"
                fill="currentColor"
              />
            </svg>
          ))}
        </div>
      </div>
    </div>
  );
}


export default App;