import React from 'react';
import "./card.css";

const Card = ({ title, postLink }) => {


  return (
    <>
      <div className="cardContainer">
        <h2 className="cardTitle">{title}</h2>
        <div className="cardLink">
          <a href={postLink}>Link</a>
        </div>
      </div>
    </>
  )
}

export default Card