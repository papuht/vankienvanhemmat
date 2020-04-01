import React, { Component } from "react";
import ReactDOM from "react-dom";
import styles from './reactstyle.css.js';
import {parseISO, formatISO} from 'date-fns';

const Background = ({background}) => {
	
	const parsed = parseISO(background.created_at, {representation: 'date'} )
	const date = formatISO(parsed,{representation: 'date'})
	
		 return (
		<div style = {styles.textstyle}>
		<ul style = {styles.liststyle}>
			<li>
			<p style = {styles.textstyleline}><b>{background.header}</b>  </p>
			<p>Julkaistu {date}</p>
			<p>Lähde: <a href ={background.link}>{background.link}</a></p><br />
			<p>{background.message}</p>
			</li>
		</ul>
	  </div>
			
		
    )
	
	



}




class Backgrounds extends Component {
  constructor(props) {
    super(props)
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    }
  }

  componentDidMount() {
    fetch("api/backgrounds")
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
	const backg = this.state.data 
    return (
	
	<div>
	{backg.map(background =>
		
        <Background key ={background.id} background = {background} />
			
			
	)}
      </div>
    )
  }
}



export default Backgrounds


