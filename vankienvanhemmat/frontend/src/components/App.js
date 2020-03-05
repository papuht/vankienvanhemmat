import React, { Component } from "react";
import { render } from "react-dom";



class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/update")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }
  
 
  

  render() {
    return (
	
      <ul>
        {this.state.data.map(update => {
          return (
		  
            <li key={update.id}>
              <p>{update.header}</p>
		      <p>Julkaistu {update.created_at}</p>
			  <p><a href ={update.link}>{update.link}</a></p><br/>
			  <p>{update.message}</p>
			  <br/>
			
			<br/>
            </li>
			
			
          );
        })}
      </ul>
	  
    );
  }
}



export default App;

const container = document.getElementById("app");
render(<App />, container);