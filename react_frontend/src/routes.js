import React from 'react';
// import Login from './views/Pages/Login/Login.js';

const Starter = React.lazy(() => import('./views/Starter/Starter.js'));
const CsvDataReader = React.lazy(() => import('./views/DataReader/CsvDataReader.js'));
const Login = React.lazy(() => import('./views/Pages/Login/Login.js'));
const Register = React.lazy(() => import('./views/Pages/Register/Register.js'));

const routes = [
  { path: '/', exact: true, name: 'Accueil' },
  { path: '/starter', name: '', component: Starter },
  { path: '/csvdatareder', name: 'Etablissements Sportifs', component: CsvDataReader },
  { path: '/Login', name: 'Connection', component: Login},
  { path: '/Register', name: 'Inscription', component: Register},

];

export default routes;
