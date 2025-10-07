import type { NextConfig } from "next";

const isDevelopment = process.env.NODE_ENV === 'development';

const nextConfig: NextConfig = {
  eslint: {
    // Disable ESLint during builds for deployment
    ignoreDuringBuilds: true,
  },
  typescript: {
    // Disable TypeScript strict checks during builds for deployment
    ignoreBuildErrors: true,
  },
  async rewrites() {
    return isDevelopment 
      ? [
          {
            source: '/api/:path*',
            destination: 'http://localhost:8000/:path*', // Proxy to local FastAPI in dev
          },
        ]
      : []; // In production, API calls go directly to /api/* (Vercel functions)
  },
  env: {
    CUSTOM_KEY: process.env.NODE_ENV || 'development',
  },
  // Configure for Vercel deployment
  experimental: {
    outputFileTracingRoot: '../',
  },
};

export default nextConfig;
