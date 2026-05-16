import React from 'react';

const Header: React.FC = () => {
  return (
    <header className="bg-indigo-600 text-white p-4 shadow-md">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-2xl font-bold">Fast Math Trainer</h1>
        <nav>
          <ul className="flex space-x-4">
            <li><a href="#" className="hover:underline">Home</a></li>
            <li><a href="#" className="hover:underline">Methods</a></li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
