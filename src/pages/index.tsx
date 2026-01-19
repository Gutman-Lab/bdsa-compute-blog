import React from 'react';
import {Redirect} from '@docusaurus/router';

export default function Home(): JSX.Element {
  // Redirect to the baseUrl root where docs/index.md with slug: / is served
  return <Redirect to="/bdsa-compute-blog/" />;
}
