export default function Dashboard() {
  return (
    <div className="w-full max-w-3xl border-2 border-cyan-400 rounded-lg p-6">
      <h2 className="text-2xl font-bold mb-3 text-cyan-400">AUDIT RESULTS</h2>
      <p className="text-cyan-300 mb-6">Smart contract analysis will be shown here.</p>
     
      {/* Added Action Buttons */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* 1. Address Input */}
        <div className="flex items-center gap-2">
          <input
            type="text"
            placeholder="Contract Address"
            className="flex-1 px-4 py-2 bg-black border border-cyan-400 rounded text-cyan-300 focus:outline-none focus:ring-2 focus:ring-cyan-500"
          />
          <button className="px-4 py-2 bg-cyan-600 hover:bg-cyan-700 text-white rounded">
            Submit
          </button>
        </div>


        {/* 3. View Report */}
        <button className="w-full px-6 py-2 bg-cyan-400 hover:bg-cyan-500 text-cyan-900 font-semibold rounded">
          View Generated Report
        </button>


        {/* 4. Save to Blockchain */}
        <button className="w-full px-6 py-2 bg-cyan-600 hover:bg-cyan-700 text-white font-semibold rounded">
          Save Audit to Blockchain
        </button>


        {/* 5. View Saved Audits */}
        <button className="w-full px-6 py-2 bg-cyan-500 hover:bg-cyan-600 text-cyan-900 font-semibold rounded">
          View Saved Audits
        </button>
      </div>
    </div>
  );
}
