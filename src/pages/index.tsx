import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';

export default function Home(): JSX.Element {
  return (
    <Layout
      title="BDSA Compute Blog"
      description="Experiment Tracking & Results for BDSA">
      <main style={{padding: '2rem'}}>
        <div style={{maxWidth: '800px', margin: '0 auto'}}>
          <h1>BDSA Compute Blog</h1>
          <p>Welcome to the <strong>BDSA Compute Blog</strong> — a comprehensive resource for tracking algorithms, performance metrics, and computational benchmarks for the <strong>BDSA</strong> (open source image analysis platform) project.</p>
          
          <h2>Quick Links</h2>
          <ul>
            <li><Link to={useBaseUrl('/docs')}>Documentation</Link> - Algorithms, experiments, and methodology</li>
            <li><Link to={useBaseUrl('/blog')}>Blog</Link> - Updates and algorithm highlights</li>
            <li><Link to={useBaseUrl('/docs/algorithms')}>Algorithms</Link> - Available BDSA functions</li>
            <li><Link to={useBaseUrl('/docs/experiments')}>Experiments</Link> - Performance metrics and results</li>
          </ul>

          <h2>What is BDSA?</h2>
          <p>BDSA is an open-source image analysis platform designed for histopathology and medical image analysis. This site provides:</p>
          <ul>
            <li>📊 <strong>Algorithm Documentation</strong> - Detailed descriptions of available functions and methods</li>
            <li>⚡ <strong>Performance Metrics</strong> - Runtime benchmarks and execution time comparisons</li>
            <li>🖥️ <strong>Hardware Comparisons</strong> - Performance across different compute environments</li>
            <li>📈 <strong>Experiment Tracking</strong> - Reproducible results and methodology documentation</li>
          </ul>

          <p><Link to={useBaseUrl('/docs')} className="button button--primary button--lg">Get Started →</Link></p>
        </div>
      </main>
    </Layout>
  );
}
