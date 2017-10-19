import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class counter extends React.Component {
  constructor(props){
    super(props);
    this.state={
      value: null,
    }
  }
    render() {
    return (
      <button className="square" onClick={() => this.setState({value: 'X'})}>
        {this.state.value}
      </button>
    );
  }
}
export default counter;