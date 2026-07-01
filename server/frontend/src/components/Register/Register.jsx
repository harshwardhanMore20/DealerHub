import React, { useState } from 'react';

const Register = () => {
  const [formData, setFormData] = useState({
    username: '',
    firstName: '',
    lastName: '',
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div style={{ maxWidth: '480px', margin: '40px auto', padding: '24px', border: '1px solid #ddd', borderRadius: '8px' }}>
      <h2>Sign Up</h2>
      <form>
        <div style={{ marginBottom: '12px' }}>
          <label>Username</label>
          <input name="username" value={formData.username} onChange={handleChange} style={{ width: '100%', padding: '8px' }} />
        </div>
        <div style={{ marginBottom: '12px' }}>
          <label>First Name</label>
          <input name="firstName" value={formData.firstName} onChange={handleChange} style={{ width: '100%', padding: '8px' }} />
        </div>
        <div style={{ marginBottom: '12px' }}>
          <label>Last Name</label>
          <input name="lastName" value={formData.lastName} onChange={handleChange} style={{ width: '100%', padding: '8px' }} />
        </div>
        <div style={{ marginBottom: '12px' }}>
          <label>Email</label>
          <input type="email" name="email" value={formData.email} onChange={handleChange} style={{ width: '100%', padding: '8px' }} />
        </div>
        <div style={{ marginBottom: '12px' }}>
          <label>Password</label>
          <input type="password" name="password" value={formData.password} onChange={handleChange} style={{ width: '100%', padding: '8px' }} />
        </div>
        <button type="button" style={{ width: '100%', padding: '10px', background: '#2563eb', color: 'white', border: 'none', borderRadius: '4px' }}>
          Register
        </button>
      </form>
    </div>
  );
};

export default Register;
