use Illuminate\Support\Facades\Auth;

public function login(Request $request)
{
    $credentials = $request->only('email', 'password');

    if (Auth::attempt($credentials)) {
        $request->session()->regenerate();
        return redirect()->intended('/filament');
    }

    return back()->withErrors([
        'email' => 'Email atau password salah.',
    ]);
}
