import React from "react";
import { FaGithub, FaLinkedin, FaInstagram } from 'react-icons/fa';

function Footer() {
  return (
    <footer className="footer">
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <h4>Connect with Us</h4>
            <ul className="list-inline">
              <li className="list-inline-item">
                <a className="social-link" href="https://github.com/hukerikar" target="_blank" rel="noopener noreferrer">
                  <FaGithub size="3em"/>
                  
                </a>
              </li>
              <li className="list-inline-item">
                <a className="social-link" href="https://www.linkedin.com/in/srujan-hukerikar-2a6172213/" target="_blank" rel="noopener noreferrer">
                  <FaLinkedin size="3em"/>
                </a>
              </li>
              <li className="list-inline-item">
                <a className="social-link" href="https://www.instagram.com/_.srujan_06_._/" target="_blank" rel="noopener noreferrer">
                  <FaInstagram size="3em"/>
                </a>
              </li>
            </ul>
          </div>
          <div className="col-md-6">
            <h4>Contact Us</h4>
            <p>Email: <a href="mailto:srujanhukerikar21@example.com">srujanhukerikar21@example.com</a></p>
            <p>Phone: 7083465918</p>
          </div>
        </div>
        <p className="text-center">&copy; {new Date().getFullYear()} Your Company Name. All Rights Reserved.</p>
        
      </div>
    </footer>
  );
}

export default Footer;
