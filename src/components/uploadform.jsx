export default function UploadForm() {
  return (
    <div className="w-full max-w-md mb-8 p-6 border-2 border-cyan-400 rounded-lg">
      <div className="flex items-center gap-4 mb-4">
        <input type="file" id="contract-upload" className="hidden" />
        <label
          htmlFor="contract-upload"
          className="px-4 py-2 bg-cyan-600 hover:bg-cyan-700 text-white rounded cursor-pointer flex items-center gap-2"
        >
          Choose .sol File
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            className="w-5 h-5"
          >
            <path
              fillRule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
              clipRule="evenodd"
            />
          </svg>
        </label>
        <span className="text-cyan-300">No file chosen</span>
      </div>
      <button className="w-full px-6 py-2 bg-cyan-400 hover:bg-cyan-500 text-cyan-900 font-semibold rounded">
        Upload & Audit
      </button>
    </div>
  );
}
