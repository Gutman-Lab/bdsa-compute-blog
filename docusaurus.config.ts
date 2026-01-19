import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'BDSA Compute Blog',
  tagline: 'Experiment Tracking & Results for BDSA',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://gutman-lab.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages, this is often /<projectName>/
  baseUrl: '/bdsa-compute-blog/',

  // GitHub pages deployment config.
  organizationName: 'Gutman-Lab',
  projectName: 'bdsa-compute-blog',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Edit the base directory of docs
          routeBasePath: 'docs',
        },
        blog: {
          showReadingTime: true,
          // Edit the base directory of blog
          routeBasePath: 'blog',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'BDSA Compute Blog',
      logo: {
        alt: 'BDSA Logo',
        src: 'img/logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Docs',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/gutman-lab/bdsa-compute-blog',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Experiments',
              to: '/docs/experiments',
            },
            {
              label: 'Methodology',
              to: '/docs/methodology',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/gutman-lab/bdsa-compute-blog',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Gutman Lab. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
