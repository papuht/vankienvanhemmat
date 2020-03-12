import React, { Component } from "react";
import ReactDOM from "react-dom";
import styles from './reactstyle.css.js';

const Background = ({background}) => {
	
	
	
		 return (
		
			<li>
			<p>{background.header}</p><br />
			<p>{background.created_at}</p><br />
			<p><a href ={backgrounds.link}>{backgrounds.link}</a></p><br />
			<p>{background.message}</p><br />
			</li>
			
		
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
	
	<div style = {styles.textstyle}>
	<ul>
	{backg.map(background =>
		
        <Background key ={background.id} background = {background} />
			
			
	)}
      </ul>
	  </div>
    )
  }
}



export default Backgrounds;

ReactDOM.render(<Backgrounds />, document.getElementById('backgrounds'))
