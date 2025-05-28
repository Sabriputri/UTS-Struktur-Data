<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class LoginController extends Controller
{
    // Tampilkan halaman form login
    public function showLoginForm()
    {
        return view('auth.login');
    }

    // Proses login
    public function login(Request $request)
    {
        // Ambil email dan password dari form
        $credentials = $request->only('email', 'password');

        // Cek data login
        if (Auth::attempt($credentials)) {
            // Jika berhasil login, redirect ke halaman dashboard
            return redirect()->intended('/dashboard');
        }

        // Jika gagal login, kembali ke halaman login dengan pesan error
        return back()->withErrors([
            'email' => 'Email atau password salah',
        ]);
    }

    // Logout user
    public function logout()
    {
        Auth::logout();
        return redirect('/login');
    }
}
