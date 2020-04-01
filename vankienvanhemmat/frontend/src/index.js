import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';
import Backgrounds from './components/Backgrounds';


if(document.getElementById("app")) {
  ReactDOM.render(<App />, document.getElementById("app"))
} 

else if(document.getElementById("backgrounds")) {
 ReactDOM.render(<Backgrounds />, document.getElementById("backgrounds"))
}