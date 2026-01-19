import React from 'react';
import {Redirect} from '@docusaurus/router';

export default function Home(): JSX.Element {
  // Redirect root to docs index
  return <Redirect to="/docs" />;
}
