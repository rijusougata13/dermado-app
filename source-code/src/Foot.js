import React from "react";
import "./App.css";

class Foot extends React.Component {
  render() {
    return (
      <div id="footer">
        <div className="row" id="footer-content">
          <a
            className="col-md-12 col-sm-12 col-lg-4"
            href=""
          >
            E-MAIL
          </a>
          <a
            className="col-md-12 col-sm-12 col-lg-4"
            href=""
          >
            GITHUB
          </a>
          <a className="col-md-12 col-sm-12 col-lg-4" href="">
            CONTACT
          </a>
        </div>
      </div>
    );
  }
}

export default Foot;
