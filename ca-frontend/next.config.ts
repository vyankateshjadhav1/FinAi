import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: process.env.NODE_ENV === 'production' 
          ? '/api/:path*'  // In production, API calls go to Vercel functions
          : 'http://localhost:8000/:path*', // In development, proxy to local FastAPI
      },
    ];
  },
  env: {
    CUSTOM_KEY: process.env.NODE_ENV,
  },
};

export default nextConfig;
