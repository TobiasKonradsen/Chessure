
import React from 'react';
import './PieceList.css';
import Piece from '../Piece/Piece';



class PieceList extends React.Component {
    render(){
      return (
        <div className="PieceList">
           {
            this.props.pieces.map(piece=>{
                return < Piece  key={piece.id} piece={piece} /> // </Piece>onAdd={this.props.onAdd} onRemove={this.props.onRemove} isRemoval={this.props.isRemoval}/>
                }
              )
          }
        </div>
      )
    };
  }


export default PieceList;