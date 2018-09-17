function [dy,xc] = Der_modified(F,x,varargin)
%DER_MODIFIED: this function calculates the first derivative as in Der.m
%file with also the choice of higher order formulas for the first
%derivative

if isempty(varargin)
   % Default method
    varargin{1} = 'cd'; 
end
if ~isnumeric(x)
    error('Second input must be numeric vector')
end
if ~isa(F,'function_handle')
    if isnumeric(F)
      xc = chop(x); % method for data depends on how you assign dy to xc
      dy = diff(F)./diff(x); 
      varargin{1} = 'data';
    else
      error('First input must be a function handle or a numeric array')
    end
end

n=length(x);
dx = diff(x);

switch varargin{1}
    case 'fd' 
        dy = (F(x(2:n)) - F(x(1:n-1)))./dx;
        xc = x(1:n-1);
    case 'bd'
        dy = (F(x(2:n)) - F(x(1:n-1)))./dx;
        xc = x(2:n);
    case 'cd'
        dy = (F(x(1:n-1)+0.5*dx) - F(x(1:n-1)-0.5*dx))./dx;
        xc = chop(x);
    case 'ed'
        half = (F(x(1:n-1)+0.25*dx) - F(x(1:n-1)-0.25*dx))./(0.5*dx); 
        full = (F(x(1:n-1)+0.5*dx) - F(x(1:n-1)-0.5*dx))./dx;
        dy = (4/3).*half - (1/3).*full;
        xc = chop(x);
    case 'cd_2ndord'
        dy = ((1/2)*F(x(3:n)) - (1/2)*F(x(1:n-2)))/.dx;
        xc = x(2:n-1);
    case 'cd_3rdord'
        dy = ((-1/24)*F(x(3:n)+0.5*dx)+(27/24)*F(x(2:n-1)+0.5*dx)-(27/24)*F(x(2:n-1)-0.5*dx)+(1/24)*F(x(1:n-2)+0.5*dx))/.dx;
        xc = x(2:n-1);
    case 'data'
        return;
    otherwise
        error('method not recognized');
end
end

end

