import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-gray-800 text-white p-6 mt-12">
      <div className="container mx-auto text-center">
        <p>&copy; {new Date().getFullYear()} Fast Math Trainer. Master Trachtenberg & Vedic Methods.</p>
      </div>
    </footer>
  );
};

export default Footer;
