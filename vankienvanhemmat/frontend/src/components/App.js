import React, { Component } from "react";
import { render } from "react-dom";
import styles from './reactstyle.css.js';

const Updates = ({data}) => {
	
	const updates = this.data.map(update =>
		<div>
			<p>{updates.header}</p>
			<p>{updates.created_at}</p>
			<p><a href ={updates.link}>{updates.link}</a></p>
			<p>{updates.message}</p>
		</div>
	)
	
		 return (
		
		<ul><li key={updates.id}>{updates}</li></ul>
		
    )
	
	



}




class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    }
  }

  componentDidMount() {
    fetch("api/update")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" }
          })
        }
        return response.json()
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          }
        })
      })
	  
  }
  
	
 
  

  render() {
    return (
	
	<div style = {styles.textstyle}>
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
			
			
          )
        })}
      </ul>
	  </div>
    )
  }
}



export default App;

const container = document.getElementById("app");
render(<App />, container);