import { useState, useRef } from 'react';

const BILLI_PATH = 'C:\\claude\\Udo-Vault\\Topics\\Agent-Bridge\\BILLI_TO_CLAUDE.md';

export default function BilliReader() {
  const [content, setContent] = useState('');
  const [copied, setCopied] = useState(false);
  const fileInputRef = useRef(null);

  const handleFileUpload = (e) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (ev) => {
        const text = ev.target?.result;
        setContent(typeof text === 'string' ? text : '');
      };
      reader.readAsText(file);
    }
  };

  const handlePaste = () => {
    navigator.clipboard.readText().then(text => {
      setContent(text);
    });
  };

  const sendToClaude = () => {
    if (content.trim()) {
      // Copy to clipboard for manual paste
      navigator.clipboard.writeText(content);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const clear = () => {
    setContent('');
    setCopied(false);
  };

  return (
    <div style={{ 
      fontFamily: 'system-ui, sans-serif', 
      maxWidth: '700px', 
      margin: '0 auto',
      padding: '20px'
    }}>
      <h2 style={{ marginBottom: '20px', color: '#1a1a2e' }}>
        Billi Reader - Obsidian Bridge
      </h2>

      <div style={{ 
        display: 'flex', 
        gap: '10px', 
        marginBottom: '15px',
        flexWrap: 'wrap'
      }}>
        <input
          type="file"
          accept=".md,.txt"
          onChange={handleFileUpload}
          ref={fileInputRef}
          style={{ display: 'none' }}
          id="billi-file"
        />
        <button 
          onClick={() => fileInputRef.current?.click()}
          style={{
            padding: '10px 20px',
            background: '#4a90d9',
            color: 'white',
            border: 'none',
            borderRadius: '8px',
            cursor: 'pointer'
          }}
        >
          Upload BILLI_TO_CLAUDE.md
        </button>
        
        <button 
          onClick={handlePaste}
          style={{
            padding: '10px 20px',
            background: '#2d2d2d',
            color: 'white',
            border: 'none',
            borderRadius: '8px',
            cursor: 'pointer'
          }}
        >
          Paste from Clipboard
        </button>

        {content && (
          <>
            <button 
              onClick={sendToClaude}
              style={{
                padding: '10px 20px',
                background: copied ? '#22c55e' : '#f59e0b',
                color: 'white',
                border: 'none',
                borderRadius: '8px',
                cursor: 'pointer'
              }}
            >
              {copied ? 'Copied! Paste to Claude' : 'Send to Claude'}
            </button>
            
            <button 
              onClick={clear}
              style={{
                padding: '10px 20px',
                background: '#ef4444',
                color: 'white',
                border: 'none',
                borderRadius: '8px',
                cursor: 'pointer'
              }}
            >
              Clear
            </button>
          </>
        )}
      </div>

      <div style={{
        border: '1px solid #e5e5e5',
        borderRadius: '8px',
        overflow: 'hidden'
      }}>
        <div style={{
          background: '#f5f5f5',
          padding: '8px 12px',
          fontSize: '12px',
          color: '#666',
          borderBottom: '1px solid #e5e5e5'
        }}>
          BILLI_TO_CLAUDE.md Content
        </div>
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
          placeholder="Upload or paste BILLI_TO_CLAUDE.md content here..."
          style={{
            width: '100%',
            minHeight: '300px',
            padding: '12px',
            border: 'none',
            resize: 'vertical',
            fontFamily: 'monospace',
            fontSize: '13px',
            lineHeight: '1.6'
          }}
        />
      </div>

      <p style={{ fontSize: '12px', color: '#888', marginTop: '10px' }}>
        Path: {BILLI_PATH}
      </p>
    </div>
  );
}
