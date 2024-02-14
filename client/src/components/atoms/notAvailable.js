import React from "react";
import logo from '../../images/logonn-transparent.png';

const divStyles = {
    paddingTop: "30vh",
    color: "white",
    margin: "auto",
    width: "40%",
    fontWeight: 300
}

const imgStyles = {
    "width": 200
}

const optionsStyles = {
    textAlign: "left"
}

function NotAvailable() {
  return (
    <div style={divStyles}>
        <img style={imgStyles} id={"logoImg"} src={logo} alt="logo" />
        <p> Deontay is only available on Mobile</p>
        <p style={optionsStyles}> 
            You may either:
            <li>Use your mobile device</li>
            <li>Use your browsers inspect tools to mimic the dimensions of a mobile device</li>
        </p>
    </div>
  );
}

export default NotAvailable;
