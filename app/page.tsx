'use client'

import Link from 'next/link'
import { useState } from 'react'

export default function Home() {
    return (
        <div className="min-h-screen flex flex-col items-center justify-center text-white">
            <div className="container text-center">
                {/* Logo */}
                <div className="mb-12">
                    <div className="text-6xl font-bold mb-4 bg-gradient-to-r from-white to-blue-200 bg-clip-text text-transparent">
                        PostureCheck
                    </div>
                    <div className="w-24 h-1 bg-gradient-to-r from-blue-400 to-purple-500 mx-auto rounded-full"></div>
                </div>

                {/* Main Card */}
                <div className="card max-w-2xl mx-auto mb-8">
                    <h1 className="text-3xl font-bold mb-6">AI-Powered Posture Monitoring</h1>

                    <div className="text-lg text-gray-200 mb-8 leading-relaxed">
                        <p className="mb-4">
                            Good posture is essential for your health and well-being. Poor posture can lead to:
                        </p>
                        <ul className="text-left max-w-md mx-auto space-y-2">
                            <li className="flex items-center">
                                <span className="text-red-400 mr-3">•</span>
                                Back and neck pain
                            </li>
                            <li className="flex items-center">
                                <span className="text-red-400 mr-3">•</span>
                                Reduced lung capacity
                            </li>
                            <li className="flex items-center">
                                <span className="text-red-400 mr-3">•</span>
                                Muscle fatigue and tension
                            </li>
                            <li className="flex items-center">
                                <span className="text-red-400 mr-3">•</span>
                                Long-term spinal problems
                            </li>
                        </ul>
                    </div>

                    <div className="mb-6">
                        <p className="text-gray-300 mb-4">
                            Our AI monitors your posture in real-time, especially when lifting heavy objects,
                            and alerts you to maintain proper form.
                        </p>
                    </div>

                    <Link href="/video" className="inline-block">
                        <button className="btn text-xl px-8 py-4">
                            🎥 Start Recording
                        </button>
                    </Link>
                </div>

                {/* Features */}
                <div className="grid md:grid-cols-3 gap-6 max-w-4xl mx-auto">
                    <div className="card text-center">
                        <div className="text-3xl mb-3">📸</div>
                        <h3 className="font-semibold mb-2">Smart Detection</h3>
                        <p className="text-sm text-gray-300">Automatically detects when you're carrying heavy items</p>
                    </div>
                    <div className="card text-center">
                        <div className="text-3xl mb-3">⚡</div>
                        <h3 className="font-semibold mb-2">Real-time Analysis</h3>
                        <p className="text-sm text-gray-300">Instant posture feedback with AI-powered analysis</p>
                    </div>
                    <div className="card text-center">
                        <div className="text-3xl mb-3">📹</div>
                        <h3 className="font-semibold mb-2">Incident Recording</h3>
                        <p className="text-sm text-gray-300">Records and replays posture incidents for review</p>
                    </div>
                </div>
            </div>
        </div>
    )
} 