# FinAI - Full Stack Deployment on Vercel

This project contains both a FastAPI backend and Next.js frontend deployed together on Vercel.

## 🏗️ Project Structure

```
FinAI/
├── api/                    # Vercel serverless functions (FastAPI backend)
│   ├── index.py           # Main API entry point
│   └── ca.py             # CA agent specific endpoint
├── agents/                # Original FastAPI backend code
├── ca-frontend/          # Next.js frontend
├── vercel.json           # Vercel deployment configuration
├── requirements.txt      # Python dependencies
└── package.json         # Root package.json for monorepo
```

## 🚀 Deployment Steps

### 1. Prerequisites
- GitHub account
- Vercel account (free tier works)
- Your code pushed to GitHub

### 2. Environment Variables
Set these in Vercel Dashboard:

**Required for Backend:**
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `AWS_S3_BUCKET_NAME`
- `CEREBRAS_API_KEY`
- `SERPER_API_KEY`

**Optional:**
- `ENCRYPTION_PASSWORD_LENGTH=32`
- `SESSION_TIMEOUT_HOURS=2`
- `MAX_FILE_SIZE_MB=30`
- `DEBUG=False`

### 3. Deploy on Vercel

#### Option A: Vercel CLI (Recommended)
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy from project root
vercel

# Follow the prompts:
# - Link to existing project? No
# - Project name: finai-app (or your choice)
# - Directory: ./
```

#### Option B: Vercel Dashboard
1. Go to https://vercel.com/dashboard
2. Click "New Project"
3. Import your GitHub repository
4. Set Root Directory to: `.` (root)
5. Framework Preset: Next.js
6. Click Deploy

### 4. Post-Deployment Setup
1. Add environment variables in Vercel Dashboard
2. Update CORS origins with your Vercel domain
3. Test all endpoints

## 🔧 Local Development

### Backend (FastAPI)
```bash
cd agents
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

### Frontend (Next.js)
```bash
cd ca-frontend
npm install
npm run dev
```

## 📝 API Endpoints
- Frontend: `https://your-app.vercel.app`
- Backend API: `https://your-app.vercel.app/api`
- Health Check: `https://your-app.vercel.app/api/health`

## 🔍 Troubleshooting

### Common Issues:
1. **Import Errors**: Make sure `mangum` is in requirements.txt
2. **CORS Issues**: Update CORS origins with your Vercel domain
3. **File Upload Issues**: Vercel has 50MB limit for serverless functions
4. **Timeout Issues**: Long-running operations may timeout (10s hobby, 60s pro)

### Solutions:
- Use external storage for large files
- Implement background job processing for long operations
- Use appropriate Python runtime version

## 📊 Monitoring
- Check Vercel Function logs in dashboard
- Monitor API response times
- Set up error tracking if needed