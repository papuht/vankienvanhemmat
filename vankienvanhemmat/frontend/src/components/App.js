import React, { Component } from "react";
import ReactDOM from "react-dom";
import styles from './reactstyle.css.js';
import { parseISO, formatISO } from 'date-fns';

const Updates = ({updates}) => {
	
	const parsed = parseISO(updates.created_at, {representation: 'date'} )
	const date = formatISO(parsed,{representation: 'date'})
	
		 return (
		<div style = {styles.textstyle}>
			<ul style = {styles.liststyle}>
			<li>
			<p style = {styles.textstyleline}><b>{updates.header}</b></p>
			<p>Julkaistu {date}</p>
			<p>Lähde: <a href ={updates.link}>{updates.link}</a></p><br />
			<p>{updates.message}</p>
			</li>
			</ul>
		</div>
		
		
		
		
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
	const updates = this.state.data 
    return (
	
	<div>
	
	{updates.map(update =>
		
        <Updates key ={update.id} updates = {update} />
			
			
	)}
      
	  </div>
    )
  }
}



export default App


